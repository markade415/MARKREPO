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
    <div className="min-h-screen bg-gradient-to-b from-amber-50 via-white to-sky-50">
      {/* Header */}
      <header className="bg-white/80 backdrop-blur-md shadow-sm sticky top-0 z-50">
        <div className="container mx-auto px-4 py-4 flex justify-between items-center">
          <div className="flex items-center gap-3">
            <div className="bg-gradient-to-br from-sky-500 to-violet-500 p-2 rounded-xl">
              <Rocket className="h-8 w-8 text-white" />
            </div>
            <div>
              <h1 className="text-xl font-bold text-gray-900">RocketShip Mission</h1>
              <p className="text-sm text-gray-600">Ade's Global Foundation Inc</p>
            </div>
          </div>
          <Button 
            onClick={() => handleDonateClick()}
            className="bg-gradient-to-r from-sky-500 to-violet-500 hover:from-sky-600 hover:to-violet-600 text-white font-semibold shadow-lg hover:shadow-xl transition-all duration-300"
          >
            Donate Now
          </Button>
        </div>
      </header>

      {/* Hero Section */}
      <section className="relative py-20 overflow-hidden">
        <div className="absolute inset-0 bg-gradient-to-r from-orange-100/50 to-sky-100/50"></div>
        <div className="container mx-auto px-4 relative z-10">
          <div className="grid md:grid-cols-2 gap-12 items-center">
            <div className="space-y-6">
              <div className="inline-block">
                <span className="bg-sky-100 text-sky-700 px-4 py-2 rounded-full text-sm font-semibold">
                  Urgent Appeal
                </span>
              </div>
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
                  className="bg-gradient-to-r from-sky-500 to-violet-500 hover:from-sky-600 hover:to-violet-600 text-white font-bold text-lg shadow-xl hover:shadow-2xl transition-all duration-300 transform hover:scale-105"
                >
                  Fuel the Rocket Ship Mission <ArrowRight className="ml-2 h-5 w-5" />
                </Button>
                <Button 
                  size="lg"
                  variant="outline"
                  onClick={() => document.getElementById('impact')?.scrollIntoView({ behavior: 'smooth' })}
                  className="border-2 border-sky-500 text-sky-600 hover:bg-sky-50 font-semibold text-lg"
                >
                  See Your Impact
                </Button>
              </div>
            </div>
            <div className="relative">
              <div className="absolute inset-0 bg-gradient-to-r from-sky-400/20 to-violet-400/20 blur-3xl"></div>
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
          <Card className="border-2 border-orange-200 shadow-xl">
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
                      <p className="text-3xl font-bold text-orange-600">{campaignData.percentComplete}%</p>
                      <p className="text-gray-600">{campaignData.donorCount} donors</p>
                    </div>
                  </div>
                  <Progress value={campaignData.percentComplete} className="h-4 bg-orange-100" />
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
            <Target className="h-16 w-16 text-orange-500 mx-auto" />
            <h2 className="text-4xl font-bold text-gray-900">Our Mission</h2>
            <p className="text-lg text-gray-700 leading-relaxed">
              At Ade's Global Foundation Inc, we believe every child deserves warmth, joy, and the chance to dream big. 
              In a school of 500 students, 60% are experiencing homelessness — yet their spirits remain bright. 
              Through our Rocket Ship donation event, we're delivering jackets, socks, books, toys, candies, and more to 
              kindergarteners ages 3–7. With your support, we can launch hope and comfort into their lives, ensuring that 
              no child faces the cold or hardship alone.
            </p>
            <p className="text-2xl font-semibold text-orange-600">
              Your gift is the rocket fuel that helps these little learners soar toward brighter futures.
            </p>
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
            {donationTiers.map((tier) => {
              const Icon = iconMap[tier.icon];
              return (
                <Card 
                  key={tier.id} 
                  className={`hover:shadow-2xl transition-all duration-300 transform hover:scale-105 cursor-pointer ${
                    tier.featured ? 'border-4 border-orange-500 relative' : 'border-2 border-gray-200'
                  }`}
                  onClick={() => handleDonateClick(tier)}
                >
                  {tier.featured && (
                    <div className="absolute -top-4 left-1/2 transform -translate-x-1/2">
                      <span className="bg-gradient-to-r from-orange-500 to-amber-500 text-white px-4 py-1 rounded-full text-sm font-bold shadow-lg">
                        Most Popular
                      </span>
                    </div>
                  )}
                  <CardHeader className="text-center">
                    <div className="bg-gradient-to-br from-orange-100 to-amber-100 w-20 h-20 rounded-full flex items-center justify-center mx-auto mb-4">
                      <Icon className="h-10 w-10 text-orange-600" />
                    </div>
                    <CardTitle className="text-3xl font-bold text-gray-900">${tier.amount}</CardTitle>
                    <CardDescription className="text-lg font-semibold text-gray-700">{tier.title}</CardDescription>
                  </CardHeader>
                  <CardContent>
                    <p className="text-center text-gray-600">{tier.description}</p>
                  </CardContent>
                </Card>
              );
            })}
          </div>
        </div>
      </section>

      {/* Donation Form */}
      {showDonationForm && (
        <section id="donation-form" className="py-20 bg-gradient-to-br from-orange-50 to-amber-50">
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
                  <School className="h-8 w-8 text-orange-500 flex-shrink-0" />
                  <div>
                    <h3 className="text-xl font-bold text-gray-900">RocketShip Mosaic Elementary</h3>
                    <p className="text-gray-600">950 Owsley Avenue, San Jose, CA 95122</p>
                  </div>
                </div>
                <div className="flex items-start gap-4">
                  <Heart className="h-8 w-8 text-orange-500 flex-shrink-0" />
                  <div>
                    <h3 className="text-xl font-bold text-gray-900">500 Students, 60% Homeless</h3>
                    <p className="text-gray-600">Supporting kindergarteners ages 3-7 with essential winter items and gifts</p>
                  </div>
                </div>
                <div className="flex items-start gap-4">
                  <Users className="h-8 w-8 text-orange-500 flex-shrink-0" />
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
                <p className="text-gray-600">Be the first to support this campaign!</p>
              </div>
            ) : (
              recentDonations.map((donation, index) => (
                <Card key={index} className="border-2 border-gray-200 hover:border-orange-300 transition-colors">
                  <CardContent className="p-6 flex justify-between items-center">
                    <div className="flex items-center gap-4">
                      <div className="bg-gradient-to-br from-orange-100 to-amber-100 w-12 h-12 rounded-full flex items-center justify-center">
                        <Heart className="h-6 w-6 text-orange-600" />
                      </div>
                      <div>
                        <p className="font-semibold text-gray-900">{donation.name}</p>
                        <p className="text-sm text-gray-600">{donation.time}</p>
                      </div>
                    </div>
                    <p className="text-2xl font-bold text-orange-600">${donation.amount}</p>
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
                <div className="bg-gradient-to-br from-orange-500 to-amber-500 p-2 rounded-xl">
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
                  <MapPin className="h-5 w-5 text-orange-400" />
                  <p className="text-gray-400">2323 Broad Way, Oakland, CA 94612</p>
                </div>
                <div className="flex items-center gap-3">
                  <Mail className="h-5 w-5 text-orange-400" />
                  <a href="mailto:customerservice@adesglobal-nonprofit.com" className="text-gray-400 hover:text-orange-400 transition-colors">
                    customerservice@adesglobal-nonprofit.com
                  </a>
                </div>
                <div className="flex items-center gap-3">
                  <Phone className="h-5 w-5 text-orange-400" />
                  <div className="text-gray-400">
                    <p>Phone: +888 681 9001</p>
                    <p>Text: 415-926-9926</p>
                    <p>Fax: (341) 300-1200</p>
                  </div>
                </div>
              </div>
            </div>
            <div>
              <h3 className="text-xl font-bold mb-4">School Location</h3>
              <div className="space-y-2">
                <p className="text-gray-400 font-semibold">RocketShip Mosaic Elementary</p>
                <p className="text-gray-400">950 Owsley Avenue</p>
                <p className="text-gray-400">San Jose, CA 95122</p>
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