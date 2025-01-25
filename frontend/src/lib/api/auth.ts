// Api call for authentication

// const BASE_URL = 'http://127.0.0.1:5000/auth'; //flask server URL

export async function login(email:string, password: string) {
    const response = await fetch('auth/login', {
        method: 'POST',
        headers: {
            'content-type': 'application/json',
        },
        body: JSON.stringify({email, password}),
    });

    if(!response.ok){
        const error = await response.json();
        throw new Error(error.error )
    }

    return response.json();

}