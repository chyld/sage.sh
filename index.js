#!/usr/bin/env node

import got from "got";

process.stdin.setEncoding("utf-8");
process.stdin.on("data", async (input) => {
    const json = {
        model: "mistral",
        stream: false,
        messages: [
            {
                role: "system",
                content:
                    "You are a zsh shell expert on linux, please help me complete the following command, you should output the completed command with a few examples. Be concise. Always use markdown syntax for your response.",
            },
            { role: "user", content: input },
        ],
    };

    try {
        const data = await got.post("http://192.168.1.139:11434/api/chat", { json });
        const response = JSON.parse(data.body).message.content;
        console.log(response);
    } catch (error) {
        console.log(error);
    }
});

