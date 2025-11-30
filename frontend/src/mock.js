// Mock data for RocketShip fundraising campaign

export const campaignData = {
  goal: 15000,
  currentAmount: 3600,
  donorCount: 48,
  percentComplete: 24.0
};

export const donationTiers = [
  {
    id: 'tier1',
    amount: 25,
    title: 'One Child',
    description: 'Provides a warm jacket and a book for one child',
    icon: 'BookOpen'
  },
  {
    id: 'tier2',
    amount: 50,
    title: 'Two Children',
    description: 'Delivers jackets, socks, and toys for two children',
    icon: 'Users',
    featured: true
  },
  {
    id: 'tier3',
    amount: 100,
    title: 'Rocket Ship of Hope',
    description: 'Brings warmth, books, and joy to four children',
    icon: 'Rocket'
  },
  {
    id: 'tier4',
    amount: 250,
    title: 'Full Classroom',
    description: 'Equips an entire classroom with jackets, books, toys, and sweet treats',
    icon: 'School'
  }
];

export const recentDonations = [
  { name: 'Sarah M.', amount: 100, time: '2 hours ago' },
  { name: 'John D.', amount: 50, time: '5 hours ago' },
  { name: 'Anonymous', amount: 250, time: '8 hours ago' },
  { name: 'Emily R.', amount: 25, time: '12 hours ago' },
  { name: 'Michael T.', amount: 100, time: '1 day ago' }
];

export const mockDonation = (amount, paymentMethod) => {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve({
        success: true,
        transactionId: `MOCK-${Date.now()}`,
        amount,
        paymentMethod,
        message: 'Thank you for your donation! (Mock payment processed)'
      });
    }, 2000);
  });
};