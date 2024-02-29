function getPayload(input) {
    return {
        model: "mistral",
        stream: false,
        messages: [
            {
                role: "system",
                content:
                    "You are a zsh and bash shell expert on linux, please help me complete the following command, you should output the completed command with a few examples. Be concise. Always use markdown syntax for your response.",
            },
            { role: "user", content: input },
        ],
    };
}

export { getPayload };
