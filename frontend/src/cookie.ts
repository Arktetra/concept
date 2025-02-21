import { browser } from "$app/environment";

export class Cookie {
    public static get(key: string): string {
        if (browser) {
            let name  = key + "=";
            let decodedCookie = decodeURIComponent(document.cookie);
            let cookies = decodedCookie.split(";");

            for (let i = 0; i < cookies.length; i++) {
                let cookie = cookies[i];

                while (cookie.charAt(0) == " ") {
                    cookie = cookie.substring(1);
                }

                if (cookie.indexOf(name) == 0) {
                    return cookie.substring(name.length, cookie.length)
                }
            }
        }

        return "";
    }
}