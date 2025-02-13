import type { PageLoad } from "./$types";

export const load: PageLoad = async ({ fetch, params }) => {
    try {
        const res = await fetch("posts/get", {
            method: "POST",
            headers: {
                "content-type": "application/json",
            },
            body: JSON.stringify({ slug: params.slug }),
        });

        if (!res.ok) {
            const error = await res.json();
            throw new Error(error.error);
        }

        let resp = await res.json();
        console.log(resp["content"]);

        return {
            title: resp["title"],
            content: resp["content"]
        }
    } catch (err) {
        console.log(err);
    }
}