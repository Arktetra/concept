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