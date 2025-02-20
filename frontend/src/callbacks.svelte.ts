import { concept, create, errorTracker, user } from "./state.svelte";
import { goto } from "$app/navigation";

export const resetErrorTracker = () => {
    errorTracker.message = "";
}

export const registerCallback = async (user_name: string, email: string, password: string, mobile: string) => {
    try {
        const res = await fetch("/accounts/register", {
            method: 'POST',
            headers: {
                'content-type': 'application/json'
            },
            body: JSON.stringify({
                user_name, email, password, mobile
            })
        });

        resetErrorTracker();

        if (!res.ok) {
            if (res.status === 409) {
                errorTracker.message = res.statusText;
                // console.log(res.statusText);
                console.log("Email already exists.")
            }

            const error = await res.json();
            errorTracker.message = error.error;
            throw new Error(error.error);
        }

        user.email = email;

        goto("/concept/");
    } catch (err) {
        console.log(err);
    }
}

export const loginCallback = async (email: string, password: string) => {
    try {
        const res = await fetch("/accounts/login", {
            method: 'POST',
            headers: {
                'content-type': 'application/json'
            },
            body: JSON.stringify({
                email, password
            })
        });

        resetErrorTracker();

        if (!res.ok) {
            if (res.status === 401) {
                console.log(res.statusText);
            }

            const error = await res.json();
            errorTracker.message = error.error;
            throw new Error(error.error);
        }

        user.email = email;

        goto("/concept/")
    } catch (err) {
        console.log(err);
    }
}

export const getConcepts = async () => {
    try {
        const res = await fetch("concepts/get");

        if (!res.ok) {
            const error = await res.json();
            throw new Error(error.error);
        }

        let data = await res.json();
        console.log(data);

        return data;
    } catch (err) {
        console.log(err);
    }
}

export const addConcept = async () => {
    try {
        const res = await fetch("/concepts/add", {
            method: 'POST',
            headers: {
                'content-type': 'application/json',
            },
            body: JSON.stringify({
                title: concept.title,
                abstract: concept.abstract,
                content: concept.content,
                author_emails: [user.email],
                tags: concept.tags.trim().split(" "),
                type: create.type
            })
        });

        if (!res.ok) {
            if (res.status === 401) {
                goto("/concept/register");
            }

            const error = await res.json();
            throw new Error(error.error)
        }

        create.success = true;
    } catch (err) {
        create.success = false;
        console.log(err);
    }
}


export const publishCallback = async () => {
    if (concept.title === "") {
        console.log("Enter a title.");
    }

    await addConcept();

    if (create.success) {
        concept.title = "";
        concept.abstract = "";
        concept.content = "";
        concept.tags = "";
    }
}

export const discardCallback = () => {
    concept.title = "";
    concept.abstract = "";
    concept.content = "";
}
