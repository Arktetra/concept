import type { PageLoad } from "./$types";

export const load: PageLoad = async ({ fetch, params }) => {
    try {
        const res = await fetch("/categories/get", {
            method: "POST",
            headers: {
                "content-type": "application/json",
            },
            body: JSON.stringify({ id: params.slug }),
        });

        if (!res.ok) {
            const error = await res.json();
            throw new Error(error.error);
        }

        let data: {
            id: number,
            title: string,
            abstract: string,
            created_at: string,
            updated_at: string,
            type: string
        }[] = await res.json();

        // console.log(data);

        return {
            posts: data
        };
    } catch (err) {
        console.log(err);
    }
}