import { post } from "../../../../state.svelte";
import type { PageLoad } from "./$types";

export const load: PageLoad = async ({ fetch, params }) => {
    try {
        post.id = params.slug

        const res = await fetch("/posts/get", {
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

        let data = await res.json();
        console.log(data["content"]);

        return {
            title: data["title"],
            abstract: data["abstract"],
            content: data["content"],
            created_at: data["created_at"],
            updated_at: data["updated_at"],
            authors: data["authors"],
            tags: data["tags"],
            comments: data["comments"],
        }
    } catch (err) {
        console.log(err);
    }
}