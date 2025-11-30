import React, { useState, useEffect } from 'react';
import { CreditCard, DollarSign, CheckCircle, Loader2 } from 'lucide-react';
import { Button } from './ui/button';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from './ui/card';
import { Input } from './ui/input';
import { Label } from './ui/label';
import { RadioGroup, RadioGroupItem } from './ui/radio-group';
import { useToast } from '../hooks/use-toast';
import { toast as sonnerToast } from 'sonner';
import { createStripeSession, pollStripeStatus } from '../services/api';

const DonationForm = ({ selectedTier, onSuccess }) => {
  const { toast } = useToast();
  const [amount, setAmount] = useState(selectedTier?.amount || '');
  const [paymentMethod, setPaymentMethod] = useState('stripe');
  const [isProcessing, setIsProcessing] = useState(false);
  const [donationComplete, setDonationComplete] = useState(false);
  const [donationAmount, setDonationAmount] = useState(0);

  // Check for returning from Stripe
  useEffect(() => {
    const checkStripeReturn = async () => {
      const urlParams = new URLSearchParams(window.location.search);
      const sessionId = urlParams.get('session_id');
      
      if (sessionId) {
        setIsProcessing(true);
        sonnerToast.info('Verifying your payment...');
        
        try {
          const result = await pollStripeStatus(sessionId);
          
          if (result.success) {
            setDonationAmount(result.status.amount);
            setDonationComplete(true);
            sonnerToast.success('Payment successful!');
            
            // Refresh campaign data
            if (onSuccess) {
              onSuccess();
            }
            
            // Clean up URL
            window.history.replaceState({}, document.title, window.location.pathname);
          } else {
            sonnerToast.error(result.message || 'Payment verification failed');
          }
        } catch (error) {
          console.error('Error verifying payment:', error);
          sonnerToast.error('Failed to verify payment. Please contact support if your donation was processed.');
        } finally {
          setIsProcessing(false);
        }
      }
    };
    
    checkStripeReturn();
  }, [onSuccess]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!amount || amount <= 0) {
      sonnerToast.error('Please enter a valid donation amount.');
      return;
    }

    if (paymentMethod === 'stripe') {
      setIsProcessing(true);
      
      try {
        // Create Stripe session
        const session = await createStripeSession(parseFloat(amount), selectedTier?.id);
        
        // Redirect to Stripe checkout
        window.location.href = session.url;
      } catch (error) {
        console.error('Error creating payment session:', error);
        sonnerToast.error('Failed to initialize payment. Please try again.');
        setIsProcessing(false);
      }
    } else if (paymentMethod === 'paypal') {
      sonnerToast.info('PayPal integration coming soon! Please use Stripe for now.');
    }
  };

  if (donationComplete) {
    return (
      <Card className="max-w-2xl mx-auto border-4 border-green-500 shadow-2xl">
        <CardContent className="p-12 text-center space-y-6">
          <div className="bg-green-100 w-24 h-24 rounded-full flex items-center justify-center mx-auto">
            <CheckCircle className="h-16 w-16 text-green-600" />
          </div>
          <h2 className="text-4xl font-bold text-gray-900">Thank You for Your Generosity!</h2>
          <p className="text-xl text-gray-700">
            Your ${donationAmount.toFixed(2)} donation will help bring warmth, joy, and hope to children who need it most.
          </p>
          <p className="text-lg text-gray-600">
            You are the rocket fuel that helps these little learners soar toward brighter futures.
          </p>
          <img 
            src="https://images.unsplash.com/photo-1763982811982-e4901b18bbe3"
            alt="Family hope"
            className="rounded-2xl shadow-xl w-full h-[300px] object-cover"
          />
          <Button 
            size="lg"
            onClick={() => window.location.reload()}
            className="bg-gradient-to-r from-orange-500 to-amber-500 hover:from-orange-600 hover:to-amber-600 text-white font-bold"
          >
            Make Another Donation
          </Button>
        </CardContent>
      </Card>
    );
  }

  return (
    <Card className="max-w-2xl mx-auto border-4 border-orange-300 shadow-2xl">
      <CardHeader className="text-center bg-gradient-to-r from-sky-100 to-violet-100">
        <CardTitle className="text-3xl font-bold text-gray-900">Complete Your Donation</CardTitle>
        <CardDescription className="text-lg text-gray-700">
          Help us reach our goal and support children in need
        </CardDescription>
      </CardHeader>
      <CardContent className="p-8">
        <form onSubmit={handleSubmit} className="space-y-6">
          {/* Amount Selection */}
          <div className="space-y-3">
            <Label htmlFor="amount" className="text-lg font-semibold text-gray-900">
              Donation Amount ($)
            </Label>
            <div className="relative">
              <DollarSign className="absolute left-3 top-1/2 transform -translate-y-1/2 h-5 w-5 text-gray-400" />
              <Input 
                id="amount"
                type="number"
                min="1"
                step="1"
                value={amount}
                onChange={(e) => setAmount(e.target.value)}
                className="pl-10 text-2xl font-bold border-2 border-sky-300 focus:border-sky-500 h-16"
                placeholder="Enter amount"
                required
              />
            </div>
            {selectedTier && (
              <p className="text-sm text-gray-600">
                {selectedTier.title}: {selectedTier.description}
              </p>
            )}
          </div>

          {/* Quick Amount Buttons */}
          <div className="grid grid-cols-4 gap-3">
            {[25, 50, 100, 250].map((presetAmount) => (
              <Button
                key={presetAmount}
                type="button"
                variant={amount == presetAmount ? "default" : "outline"}
                onClick={() => setAmount(presetAmount)}
                className={amount == presetAmount ? "bg-sky-500 hover:bg-sky-600" : "border-sky-300 hover:bg-sky-50"}
              >
                ${presetAmount}
              </Button>
            ))}
          </div>

          {/* Payment Method */}
          <div className="space-y-3">
            <Label className="text-lg font-semibold text-gray-900">Payment Method</Label>
            <RadioGroup value={paymentMethod} onValueChange={setPaymentMethod}>
              <div className="flex items-center space-x-3 border-2 border-gray-200 rounded-lg p-4 hover:border-orange-300 transition-colors">
                <RadioGroupItem value="stripe" id="stripe" />
                <Label htmlFor="stripe" className="flex-1 cursor-pointer flex items-center gap-3">
                  <CreditCard className="h-5 w-5 text-gray-600" />
                  <div>
                    <p className="font-semibold text-gray-900">Credit/Debit Card</p>
                    <p className="text-sm text-gray-600">Powered by Stripe</p>
                  </div>
                </Label>
              </div>
              <div className="flex items-center space-x-3 border-2 border-gray-200 rounded-lg p-4 hover:border-orange-300 transition-colors">
                <RadioGroupItem value="paypal" id="paypal" />
                <Label htmlFor="paypal" className="flex-1 cursor-pointer flex items-center gap-3">
                  <svg className="h-5 w-5" viewBox="0 0 24 24" fill="#003087">
                    <path d="M20.067 8.478c.492.88.556 2.014.3 3.327-.74 3.806-3.276 5.12-6.514 5.12h-.5a.805.805 0 0 0-.796.698l-.04.22-.63 3.993-.032.17a.804.804 0 0 1-.795.697H7.93c-.43 0-.747-.37-.677-.787l2.062-13.063a.996.996 0 0 1 .984-.86h4.92c1.888 0 3.155.393 3.847 1.486z"/>
                    <path fill="#009cde" d="M11.064 3.103a.996.996 0 0 1 .984-.86h4.92c1.888 0 3.155.393 3.847 1.486.492.88.556 2.014.3 3.327-.74 3.806-3.276 5.12-6.514 5.12h-.5a.805.805 0 0 0-.796.698l-.04.22-.63 3.993-.032.17a.804.804 0 0 1-.795.697H7.93c-.43 0-.747-.37-.677-.787l2.062-13.063z"/>
                  </svg>
                  <div>
                    <p className="font-semibold text-gray-900">PayPal</p>
                    <p className="text-sm text-gray-600">Fast & secure</p>
                  </div>
                </Label>
              </div>
            </RadioGroup>
          </div>

          {/* Submit Button */}
          <Button 
            type="submit"
            size="lg"
            disabled={isProcessing}
            className="w-full bg-gradient-to-r from-orange-500 to-amber-500 hover:from-orange-600 hover:to-amber-600 text-white font-bold text-xl h-16 shadow-xl hover:shadow-2xl transition-all duration-300"
          >
            {isProcessing ? (
              <>
                <Loader2 className="mr-2 h-6 w-6 animate-spin" />
                Processing...
              </>
            ) : (
              `Donate $${amount || '0'} Now`
            )}
          </Button>

          <p className="text-center text-sm text-gray-600">
            🔒 Your payment information is secure and encrypted
          </p>
        </form>
      </CardContent>
    </Card>
  );
};

export default DonationForm;