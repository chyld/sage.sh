#!/usr/bin/env node

import got from "got";
import { getPayload } from "./payload.js";

process.stdin.setEncoding("utf-8");
process.stdin.on("data", async (input) => {
    try {
        const data = await got.post("http://192.168.1.139:11434/api/chat", { json: getPayload(input) });
        const response = JSON.parse(data.body).message.content;
        console.log(response);
    } catch (error) {
        console.log(error);
    }
});

