import { error } from "@sveltejs/kit";
import type { PageLoad } from "./$types";

export const load: PageLoad = ({ params }) => {
    if (params.slug === "hello-world") {
        return {
            title: "Hello world!",
            content: "Welcome to our blog. This contains nothing at the moment."
        };
    }

    error(404, "Not found");
}