// API call for user registration

export async function register(userData: {
    user_name: string;
    email: string;
    password: string;
    mobile?: string;
    role?: string;
  }) {
    const response = await fetch('/auth/register', {
      method: 'POST',
      headers: {
        'content-type': 'application/json',
      },
      body: JSON.stringify(userData),
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.error);
    }

    return response.json();
  }
