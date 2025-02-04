import { useRouter } from 'next/router';
import axios from 'axios';

export default function Home() {
  const router = useRouter();

  const handleLogin = () => {
    const redirectUri = encodeURIComponent(`${window.location.origin}/callback`);
    window.location.href = `${process.env.NEXT_PUBLIC_SSO_URL}/login?redirect_uri=${redirectUri}`;
  };

  return (
    <div className="container">
      <h1>AMDB Materials Database</h1>
      <button onClick={handleLogin} className="login-button">
        Login with SSO
      </button>
    </div>
  );
}