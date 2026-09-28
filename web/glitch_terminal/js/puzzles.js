const PUZZLES = {
    1: {
        name: "The Basics",
        hint: "Try typing 'help' to see available commands.",
        solution: "ACCESS_CODE_42",
        setup: () => {
            return "System: Welcome. Type 'ls' to see files, 'cat <file>' to read them.";
        },
        validate: (input) => {
            return input.trim().toUpperCase() === "ACCESS_CODE_42";
        }
    },
    2: {
        name: "The Ancient Code",
        hint: "Shift the letters back by 3 (Caesar Cipher). KHOOR ZRUOG -> HELLO WORLD",
        solution: "SECRET_KEY_77",
        setup: () => {
            return "System: A corrupted log was found. Decrypt it: 'VHFUHW NHB 77'";
        },
        validate: (input) => {
            return input.trim().toUpperCase() === "SECRET_KEY_77";
        }
    },
    3: {
        name: "The Logical Loop",
        hint: "I have keys but no locks. I have space but no room. You can enter, but never leave.",
        solution: "keyboard",
        setup: () => {
            return "System: To bypass the firewall, answer the riddle: 'I have keys but no locks. I have space but no room. You can enter, but never leave.'";
        },
        validate: (input) => {
            return input.trim().toLowerCase() === "keyboard";
        }
    },
    4: {
        name: "Memory Leak",
        hint: "Find the specific hex sequence 0xDEADBEEF among the noise.",
        solution: "0xDEADBEEF",
        setup: () => {
            const noise = Array.from({length: 20}, () => Math.floor(Math.random()*16777215).toString(16).toUpperCase()).join(' ');
            return `System: Memory Dump initiated... \n${noise} \n0xDEADBEEF \n${noise}`;
        },
        validate: (input) => {
            return input.trim().toUpperCase() === "0xDEADBEEF";
        }
    },
    5: {
        name: "The System Crash",
        hint: "The system is unstable. Type the override command exactly: 'SYSTEM_OVERRIDE_NOW'",
        solution: "SYSTEM_OVERRIDE_NOW",
        setup: () => {
            return "System: CRITICAL ERROR. Input the override code immediately to stop the wipe!";
        },
        validate: (input) => {
            return input.trim().toUpperCase() === "SYSTEM_OVERRIDE_NOW";
        }
    }
};

function validateAnswer(level, input) {
    if (PUZZLES[level]) {
        return PUZZLES[level].validate(input);
    }
    return false;
}
