import { redirect } from "@sveltejs/kit";
import { user } from "../state.svelte";

export function load() {
    if (!user.session) {
        redirect(307, "/login")
    } else {
        redirect(307, "/home")
    }
}