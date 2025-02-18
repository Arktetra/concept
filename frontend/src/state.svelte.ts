export const user = $state({
    session: false,
    email: "",
});

export const create = $state({
    clicked: false,
    type: "",
    success: true
});

export const errorTracker = $state({
    message: ""
})

export const concept = $state({
    title: "",
    abstract: "",
    content: ""
});