const ASSERTIONS = [
    {
        level: 1,
        input: "ACCESS_CODE_42",
        expected: true,
        message: "Level 1: Should accept ACCESS_CODE_42"
    },
    {
        level: 1,
        input: "WRONG_CODE",
        expected: false,
        message: "Level 1: Should reject WRONG_CODE"
    },
    {
        level: 2,
        input: "SECRET_KEY_77",
        expected: true,
        message: "Level 2: Should accept SECRET_KEY_77"
    },
    {
        level: 3,
        input: "keyboard",
        expected: true,
        message: "Level 3: Should accept 'keyboard'"
    },
    {
        level: 4,
        input: "0xDEADBEEF",
        expected: true,
        message: "Level 4: Should accept 0xDEADBEEF"
    },
    {
        level: 5,
        input: "SYSTEM_OVERRIDE_NOW",
        expected: true,
        message: "Level 5: Should accept SYSTEM_OVERRIDE_NOW"
    }
];

function runTests() {
    let passed = 0;
    const results = [];

    ASSERTIONS.forEach(test => {
        const actual = validateAnswer(test.level, test.input);
        const isPass = actual === test.expected;
        if (isPass) passed++;
        results.push({
            message: test.message,
            status: isPass ? "✅ PASS" : "❌ FAIL",
            actual: actual,
            expected: test.expected
        });
    });

    return {
        total: ASSERTIONS.length,
        passed: passed,
        details: results
    };
}
