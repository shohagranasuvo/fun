const terminalOutput = document.getElementById('output');
const commandInput = document.getElementById('command-input');
const terminalContainer = document.getElementById('terminal');

let currentLevel = 1;
let isTyping = false;

const SARCASTIC_REPLIES = [
    "Wrong. Again. I'm actually impressed by how wrong you are.",
    "Is that really your best guess? Yikes.",
    "My CPU is literally slowing down just processing your incorrect answer.",
    "Incorrect. Maybe try using your brain this time?",
    "Do you just type random letters? It feels like you do.",
    "Error 404: Intelligence not found."
];

function printToTerminal(text, delay = 20, isGlitch = false) {
    const div = document.createElement('div');
    div.className = isGlitch ? 'glitch' : '';
    terminalOutput.appendChild(div);

    let i = 0;
    const interval = setInterval(() => {
        div.textContent += text[i];
        i++;
        if (i >= text.length) {
            clearInterval(interval);
            terminalOutput.scrollTop = terminalOutput.scrollHeight;
        }
    }, delay);
}

function handleCommand(input) {
    const cmd = input.trim();

    if (cmd === "") return;

    if (cmd === "help") {
        printToTerminal("Available commands: help, clear, ls, cat <file>");
        return;
    }

    if (cmd === "clear") {
        terminalOutput.innerHTML = "";
        return;
    }

    if (cmd === "ls") {
        if (currentLevel === 1) {
            printToTerminal("welcome.txt, secret_code.txt");
            return;
        }
        printToTerminal("system_logs.txt, override_config.bin");
        return;
    }

    if (cmd.startsWith("cat ")) {
        const file = cmd.substring(4);
        if (currentLevel === 1 && file === "welcome.txt") {
            printToTerminal("Welcome to the Forbidden Server. The access code is ACCESS_CODE_42.");
            return;
        }
        printToTerminal(`File ${file} not found or access denied.`);
        return;
    }

    // Puzzle Validation
    if (validateAnswer(currentLevel, cmd)) {
        currentLevel++;
        const msg = `\n🎉 Level ${currentLevel - 1} Complete! \n`;
        printToTerminal(msg, 40);

        if (currentLevel > 5) {
            printToTerminal("\n🏆 SYSTEM BREACHED! You have successfully hacked the Forbidden Server. \nCongratulations, you are now officially a danger to society. \nGoodbye!", 60);
            commandInput.disabled = true;
            return;
        }

        printToTerminal(`\nLevel ${currentLevel}: ${PUZZLES[currentLevel].name}\n`, 40);
        printToTerminal(PUZZLES[currentLevel].setup(), 30);
    } else {
        const reply = SARCASTIC_REPLIES[Math.floor(Math.random() * SARCASTIC_REPLIES.length)];
        printToTerminal(`\n❌ ${reply}\n`, 30);
        printToTerminal(`Hint: ${PUZZLES[currentLevel].hint}\n`, 30);
    }
}

// Initialize Game
window.onload = () => {
    printToTerminal("Initializing Forbidden Server Terminal... [OK]", 50);
    setTimeout(() => {
        printToTerminal("\nAccessing Secure Shell... [OK]", 50);
        setTimeout(() => {
            printToTerminal("\nWARNING: Unauthorized access detected. Monitoring system active.", 50);
            setTimeout(() => {
                printToTerminal("\nLevel 1: The Basics\n", 40);
                printToTerminal(PUZZLES[1].setup(), 30);
            }, 1000);
        }, 1000);
    }, 1000);
};

commandInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
        const input = commandInput.value;

        // Echo command
        const echo = document.createElement('div');
        echo.className = 'input-line';
        echo.innerHTML = `<span class="prompt">guest@forbidden-server:~$</span> ${input}`;
        terminalOutput.appendChild(echo);

        handleCommand(input);
        commandInput.value = '';
    }
});
