import axios from 'axios';

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
const API = `${BACKEND_URL}/api`;

// Campaign Stats API
export const getCampaignStats = async () => {
  try {
    const response = await axios.get(`${API}/donations/stats`);
    return response.data;
  } catch (error) {
    console.error('Error fetching campaign stats:', error);
    throw error;
  }
};

// Recent Donations API
export const getRecentDonations = async () => {
  try {
    const response = await axios.get(`${API}/donations/recent`);
    return response.data;
  } catch (error) {
    console.error('Error fetching recent donations:', error);
    throw error;
  }
};

// Stripe Payment APIs
export const createStripeSession = async (amount, tierId = null) => {
  try {
    const response = await axios.post(`${API}/donations/stripe/create-session`, {
      amount,
      tier_id: tierId
    });
    return response.data;
  } catch (error) {
    console.error('Error creating Stripe session:', error);
    throw error;
  }
};

export const getStripeStatus = async (sessionId) => {
  try {
    const response = await axios.get(`${API}/donations/stripe/status/${sessionId}`);
    return response.data;
  } catch (error) {
    console.error('Error fetching Stripe status:', error);
    throw error;
  }
};

// Poll Stripe payment status
export const pollStripeStatus = async (sessionId, maxAttempts = 10, interval = 2000) => {
  for (let attempt = 0; attempt < maxAttempts; attempt++) {
    try {
      const status = await getStripeStatus(sessionId);
      
      if (status.payment_status === 'paid') {
        return { success: true, status };
      } else if (status.status === 'expired') {
        return { success: false, status, message: 'Payment session expired' };
      }
      
      // Wait before next attempt
      await new Promise(resolve => setTimeout(resolve, interval));
    } catch (error) {
      console.error(`Attempt ${attempt + 1} failed:`, error);
      if (attempt === maxAttempts - 1) {
        throw error;
      }
    }
  }
  
  throw new Error('Payment verification timed out');
};