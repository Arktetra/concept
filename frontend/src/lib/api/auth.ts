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

    return response;
}