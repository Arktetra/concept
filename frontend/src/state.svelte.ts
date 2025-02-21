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

// to add concept
export const concept = $state({
    title: "",
    abstract: "",
    content: "",
    tags: "",
});

// used when displaying posts
export const post = $state({
    id: ""
})