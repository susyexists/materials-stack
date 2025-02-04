import { useEffect } from 'react';
import { useRouter } from 'next/router';
import axios from 'axios';
import Cookies from 'universal-cookie';

export default function Callback() {
  const router = useRouter();
  const cookies = new Cookies();

  useEffect(() => {
    const authenticate = async () => {
      const code = new URLSearchParams(window.location.search).get('code');
      
      try {
        const response = await axios.post(
          `${process.env.NEXT_PUBLIC_SSO_URL}/auth/token`,
          { code }
        );

        // Store token in secure cookie
        cookies.set('access_token', response.data.token, {
          path: '/',
          secure: true,
          sameSite: 'strict',
        });

        router.push('/');
      } catch (error) {
        console.error('Authentication failed:', error);
        router.push('/error');
      }
    };

    authenticate();
  }, []);

  return <div>Authenticating...</div>;
}