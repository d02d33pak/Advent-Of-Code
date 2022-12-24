import fs from "fs/promises";

const parseInput = async (filename) => {
  let data = await fs.readFile(filename, "utf-8");
  data = data.trim().split("\n");
  return data;
};

const part1 = async (filename) => {
    const inputs = await parseInput(filename);
    let largestSum, currSum = 0;
    inputs.forEach((input) => {});
};

part1("input");
