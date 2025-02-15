import { concept } from "./state.svelte";

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

export const addConcepts = async () => {
    try {
        const res = await fetch("/concepts/add", {
            method: 'POST',
            headers: {
                'content-type': 'application/json',
            },
            body: JSON.stringify({
                title: concept.title,
                abstract: concept.abstract,
                content: concept.content
            })
        });

        if (!res.ok) {
            const error = await res.json();
            throw new Error(error.error)
        }
    } catch (err) {
        console.log(err);
    }
}
