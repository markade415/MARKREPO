import React, { useState, useEffect } from 'react';
import { Heart, Rocket, Users, BookOpen, School, Target, ArrowRight, Phone, Mail, MapPin } from 'lucide-react';
import { Button } from '../components/ui/button';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '../components/ui/card';
import { Progress } from '../components/ui/progress';
import DonationForm from '../components/DonationForm';
import { donationTiers } from '../mock';
import { getCampaignStats, getRecentDonations } from '../services/api';

const LandingPage = () => {
  const [showDonationForm, setShowDonationForm] = useState(false);
  const [selectedTier, setSelectedTier] = useState(null);
  const [campaignData, setCampaignData] = useState({
    goal: 18500,
    currentAmount: 12000,
    donorCount: 187,
    percentComplete: 64.9
  });
  const [recentDonations, setRecentDonations] = useState([]);
  const [loading, setLoading] = useState(true);

  // Fetch campaign stats and recent donations
  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        const [stats, donations] = await Promise.all([
          getCampaignStats(),
          getRecentDonations()
        ]);
        
        setCampaignData({
          goal: stats.goal,
          currentAmount: stats.current_amount,
          donorCount: stats.donor_count,
          percentComplete: stats.percent_complete
        });
        
        setRecentDonations(donations);
      } catch (error) {
        console.error('Error fetching data:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  // Refresh data after donation
  const refreshData = async () => {
    try {
      const [stats, donations] = await Promise.all([
        getCampaignStats(),
        getRecentDonations()
      ]);
      
      setCampaignData({
        goal: stats.goal,
        currentAmount: stats.current_amount,
        donorCount: stats.donor_count,
        percentComplete: stats.percent_complete
      });
      
      setRecentDonations(donations);
    } catch (error) {
      console.error('Error refreshing data:', error);
    }
  };

  const handleDonateClick = (tier = null) => {
    setSelectedTier(tier);
    setShowDonationForm(true);
    // Smooth scroll to donation form
    setTimeout(() => {
      document.getElementById('donation-form')?.scrollIntoView({ behavior: 'smooth' });
    }, 100);
  };

  const iconMap = {
    BookOpen: BookOpen,
    Users: Users,
    Rocket: Rocket,
    School: School
  };

  return (
    <div className="min-h-screen bg-gradient-to-b from-rose-50 via-white to-teal-50">
      {/* Header */}
      <header className="bg-white/80 backdrop-blur-md shadow-sm sticky top-0 z-50">
        <div className="container mx-auto px-4 py-4">
          <div className="flex justify-between items-center">
            <div className="flex items-center gap-3">
              <div className="bg-gradient-to-br from-blue-600 to-blue-400 p-2 rounded-xl">
                <Rocket className="h-8 w-8 text-white" />
              </div>
              <div>
                <h1 className="text-2xl font-bold text-gray-900">Ade's Global Foundation Inc</h1>
                <p className="text-xs text-gray-600">rocketship mission</p>
              </div>
            </div>
            
            <div className="hidden lg:block flex-1 px-8">
              <p className="text-center text-base font-bold text-transparent bg-clip-text bg-gradient-to-r from-blue-700 to-blue-500 tracking-wide">
                IT'S AN HONOR TO GIVE BACK TO THE COMMUNITY
              </p>
            </div>
            
            <div className="flex items-center gap-4">
              <a 
                href="https://adesglobal-nonprofit.com/" 
                target="_blank" 
                rel="noopener noreferrer"
                className="hidden sm:flex items-center gap-2 text-gray-700 hover:text-blue-600 font-medium transition-colors duration-300"
              >
                <svg className="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 919-9" />
                </svg>
                <span>Our Website</span>
              </a>
              <Button 
                onClick={() => handleDonateClick()}
                className="bg-gradient-to-r from-blue-600 to-blue-400 hover:from-rose-600 hover:to-teal-600 text-white font-semibold shadow-lg hover:shadow-xl transition-all duration-300"
              >
                Donate Now
              </Button>
            </div>
          </div>
        </div>
      </header>

      {/* Hero Section */}
      <section className="relative py-20 overflow-hidden">
        <div className="absolute inset-0 bg-gradient-to-r from-blue-100/50 to-sky-100/50"></div>
        <div className="container mx-auto px-4 relative z-10">
          <div className="grid md:grid-cols-2 gap-12 items-center">
            <div className="space-y-6">
              <h2 className="text-5xl md:text-6xl font-bold text-gray-900 leading-tight">
                We Inspire Young Learners Soar Higher
              </h2>
              <p className="text-xl text-gray-700 leading-relaxed">
                60% of these little learners are homeless — your gift is the rocket fuel they need to thrive.
              </p>
              <div className="flex flex-col sm:flex-row gap-4">
                <Button 
                  size="lg"
                  onClick={() => handleDonateClick()}
                  className="bg-gradient-to-r from-blue-600 to-blue-400 hover:from-sky-600 hover:to-violet-600 text-white font-bold text-lg shadow-xl hover:shadow-2xl transition-all duration-300 transform hover:scale-105"
                >
                  Fuel the Rocket Ship Mission <ArrowRight className="ml-2 h-5 w-5" />
                </Button>
                <Button 
                  size="lg"
                  variant="outline"
                  onClick={() => document.getElementById('impact')?.scrollIntoView({ behavior: 'smooth' })}
                  className="border-2 border-blue-500 text-blue-600 hover:bg-blue-50 font-semibold text-lg"
                >
                  See Your Impact
                </Button>
              </div>
            </div>
            <div className="relative">
              <div className="absolute inset-0 bg-gradient-to-r from-blue-400/20 to-sky-400/20 blur-3xl"></div>
              <img 
                src="https://images.unsplash.com/photo-1588072432836-e10032774350"
                alt="Child learning in school"
                className="rounded-3xl shadow-2xl relative z-10 w-full h-[400px] object-cover"
              />
            </div>
          </div>
        </div>
      </section>

      {/* Progress Tracker */}
      <section className="py-12 bg-white">
        <div className="container mx-auto px-4">
          <Card className="border-2 border-blue-200 shadow-xl">
            <CardContent className="p-8">
              {loading ? (
                <div className="text-center py-8">
                  <p className="text-gray-600">Loading campaign progress...</p>
                </div>
              ) : (
                <>
                  <div className="flex justify-between items-center mb-4">
                    <div>
                      <h3 className="text-3xl font-bold text-gray-900">${campaignData.currentAmount.toLocaleString()}</h3>
                      <p className="text-gray-600">raised of ${campaignData.goal.toLocaleString()} goal</p>
                    </div>
                    <div className="text-right">
                      <p className="text-3xl font-bold text-blue-600">{campaignData.percentComplete}%</p>
                      <p className="text-gray-600">{campaignData.donorCount} donors</p>
                    </div>
                  </div>
                  <Progress value={campaignData.percentComplete} className="h-4 bg-blue-100" />
                </>
              )}
            </CardContent>
          </Card>
        </div>
      </section>

      {/* Mission Statement */}
      <section className="py-20 bg-gradient-to-br from-sky-50 to-blue-50">
        <div className="container mx-auto px-4">
          <div className="max-w-4xl mx-auto text-center space-y-6">
            <Target className="h-16 w-16 text-blue-500 mx-auto" />
            <h2 className="text-4xl font-bold text-gray-900">Our Mission</h2>
            <p className="text-lg text-gray-700 leading-relaxed">
              At Ade's Global Foundation Inc, we believe every child deserves warmth, joy, and the chance to dream big. 
              In a school of 500 students, 60% are experiencing homelessness — yet their spirits remain bright. 
              Through our Rocket Ship donation event, we're delivering jackets, socks, books, toys, candies, and more to 
              kindergarteners ages 3–7. With your support, we can launch hope and comfort into their lives, ensuring that 
              no child faces the cold or hardship alone.
            </p>
            <div className="mt-8">
              <img 
                src="https://images.unsplash.com/photo-1532629345422-7515f3d16bb6?w=800"
                alt="Helping homeless with donations"
                className="rounded-2xl shadow-2xl w-full h-[300px] object-cover"
              />
            </div>
          </div>
        </div>
      </section>

      {/* Impact Statement */}
      <section id="impact" className="py-20 bg-white">
        <div className="container mx-auto px-4">
          <div className="text-center mb-12">
            <h2 className="text-4xl font-bold text-gray-900 mb-4">Your Impact</h2>
            <p className="text-xl text-gray-600">Choose your level of support</p>
          </div>
          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
            {donationTiers.map((tier, index) => {
              const Icon = iconMap[tier.icon];
              const tierImages = [
                'https://images.unsplash.com/photo-1662787271649-8843cc38454a?w=400',
                'https://images.unsplash.com/photo-1654931800100-2ecf6eee7c64?w=400',
                'https://images.unsplash.com/photo-1696563541384-bf48ecbaac45?w=400',
                'https://images.pexels.com/photos/159644/art-supplies-brushes-rulers-scissors-159644.jpeg?w=400'
              ];
              
              return (
                <Card 
                  key={tier.id} 
                  className={`hover:shadow-2xl transition-all duration-300 transform hover:scale-105 cursor-pointer overflow-hidden ${
                    tier.featured ? 'border-4 border-blue-500 relative' : 'border-2 border-gray-200'
                  }`}
                  onClick={() => handleDonateClick(tier)}
                >
                  {tier.featured && (
                    <div className="absolute -top-4 left-1/2 transform -translate-x-1/2 z-10">
                      <span className="bg-gradient-to-r from-blue-600 to-blue-400 text-white px-4 py-1 rounded-full text-sm font-bold shadow-lg">
                        Most Popular
                      </span>
                    </div>
                  )}
                  <div className="relative h-48 overflow-hidden">
                    <img 
                      src={tierImages[index]} 
                      alt={tier.title}
                      className="w-full h-full object-cover"
                    />
                    <div className="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent"></div>
                    <div className="absolute bottom-3 left-3 right-3">
                      <div className="bg-white/90 backdrop-blur-sm rounded-full px-4 py-2 flex items-center justify-center gap-2">
                        <Icon className="h-6 w-6 text-blue-600" />
                        <span className="text-2xl font-bold text-gray-900">${tier.amount}</span>
                      </div>
                    </div>
                  </div>
                  <CardHeader className="text-center pt-4">
                    <CardTitle className="text-xl font-bold text-gray-900">{tier.title}</CardTitle>
                  </CardHeader>
                  <CardContent className="pt-0">
                    <p className="text-center text-gray-600 text-sm">{tier.description}</p>
                  </CardContent>
                </Card>
              );
            })}
          </div>
        </div>
      </section>

      {/* Donation Form */}
      {showDonationForm && (
        <section id="donation-form" className="py-20 bg-gradient-to-br from-blue-50 to-sky-50">
          <div className="container mx-auto px-4">
            <DonationForm selectedTier={selectedTier} onSuccess={refreshData} />
          </div>
        </section>
      )}

      {/* Event Details */}
      <section className="py-20 bg-white">
        <div className="container mx-auto px-4">
          <div className="grid md:grid-cols-2 gap-12">
            <div>
              <img 
                src="https://images.unsplash.com/photo-1588075592405-d3d4f0846961"
                alt="Children in classroom"
                className="rounded-3xl shadow-2xl w-full h-[400px] object-cover"
              />
            </div>
            <div className="space-y-6">
              <h2 className="text-4xl font-bold text-gray-900">About the Event</h2>
              <div className="space-y-4">
                <div className="flex items-start gap-4">
                  <Heart className="h-8 w-8 text-blue-500 flex-shrink-0" />
                  <div>
                    <h3 className="text-xl font-bold text-gray-900">500 Students, 60% Homeless</h3>
                    <p className="text-gray-600">Supporting kindergarteners ages 3-7 with essential winter items and gifts</p>
                  </div>
                </div>
                <div className="flex items-start gap-4">
                  <Users className="h-8 w-8 text-blue-500 flex-shrink-0" />
                  <div>
                    <h3 className="text-xl font-bold text-gray-900">Community Effort</h3>
                    <p className="text-gray-600">Join us in making a difference, one child at a time</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Recent Donations */}
      <section className="py-20 bg-gradient-to-br from-sky-50 to-blue-50">
        <div className="container mx-auto px-4">
          <h2 className="text-4xl font-bold text-gray-900 text-center mb-12">Recent Supporters</h2>
          <div className="max-w-2xl mx-auto space-y-4">
            {loading ? (
              <div className="text-center py-8">
                <p className="text-gray-600">Loading recent donations...</p>
              </div>
            ) : recentDonations.length === 0 ? (
              <div className="text-center py-8">
                <p className="text-2xl font-bold text-blue-600">Fuel The Rocketship Mission</p>
              </div>
            ) : (
              recentDonations.map((donation, index) => (
                <Card key={index} className="border-2 border-gray-200 hover:border-blue-300 transition-colors">
                  <CardContent className="p-6 flex justify-between items-center">
                    <div className="flex items-center gap-4">
                      <div className="bg-gradient-to-br from-blue-100 to-sky-100 w-12 h-12 rounded-full flex items-center justify-center">
                        <Heart className="h-6 w-6 text-blue-600" />
                      </div>
                      <div>
                        <p className="font-semibold text-gray-900">{donation.name}</p>
                        <p className="text-sm text-gray-600">{donation.time}</p>
                      </div>
                    </div>
                    <p className="text-2xl font-bold text-blue-600">${donation.amount}</p>
                  </CardContent>
                </Card>
              ))
            )}
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gray-900 text-white py-12">
        <div className="container mx-auto px-4">
          <div className="grid md:grid-cols-3 gap-8">
            <div>
              <div className="flex items-center gap-3 mb-4">
                <div className="bg-gradient-to-br from-blue-600 to-blue-400 p-2 rounded-xl">
                  <Rocket className="h-6 w-6 text-white" />
                </div>
                <h3 className="text-xl font-bold">Ade's Global Foundation Inc</h3>
              </div>
              <p className="text-gray-400">
                We are committed to fostering a supportive environment that empowers resilient youth to thrive and realize their full potential.
              </p>
            </div>
            <div>
              <h3 className="text-xl font-bold mb-4">Contact Us</h3>
              <div className="space-y-3">
                <div className="flex items-center gap-3">
                  <MapPin className="h-5 w-5 text-blue-400" />
                  <p className="text-gray-400">2323 Broad Way, Oakland, CA 94612</p>
                </div>
                <div className="flex items-center gap-3">
                  <Mail className="h-5 w-5 text-blue-400" />
                  <a href="mailto:customerservice@adesglobal-nonprofit.com" className="text-gray-400 hover:text-blue-400 transition-colors">
                    customerservice@adesglobal-nonprofit.com
                  </a>
                </div>
                <div className="flex items-center gap-3">
                  <svg className="h-5 w-5 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9" />
                  </svg>
                  <a href="https://adesglobal-nonprofit.com/" target="_blank" rel="noopener noreferrer" className="text-gray-400 hover:text-blue-400 transition-colors">
                    adesglobal-nonprofit.com
                  </a>
                </div>
                <div className="flex items-center gap-3">
                  <Phone className="h-5 w-5 text-blue-400" />
                  <div className="text-gray-400">
                    <p>Phone: +888 681 9001</p>
                    <p>Text: 415-926-9926</p>
                    <p>Fax: (341) 300-1200</p>
                  </div>
                </div>
              </div>
            </div>
            <div>
              <h3 className="text-xl font-bold mb-4">Our Location</h3>
              <div className="space-y-3">
                <p className="text-gray-400 font-semibold">Ade's Global Foundation Inc</p>
                <p className="text-gray-400">2323 Broad Way<br/>Oakland, CA 94612</p>
                <div className="mt-4">
                  <a 
                    href="https://www.google.com/maps/search/?api=1&query=2323+Broad+Way+Oakland+CA+94612" 
                    target="_blank" 
                    rel="noopener noreferrer"
                    className="inline-flex items-center gap-2 text-blue-400 hover:text-blue-300 transition-colors"
                  >
                    <MapPin className="h-5 w-5" />
                    <span>View on Map</span>
                  </a>
                </div>
              </div>
            </div>
          </div>
          <div className="border-t border-gray-800 mt-8 pt-8 text-center">
            <p className="text-gray-400">© 2025 Ade's Global Foundation Inc. All rights reserved.</p>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default LandingPage;