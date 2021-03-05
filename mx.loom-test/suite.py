suite = {
    "mxversion": "5.285.10",
    "name": "loom-test",

    "imports": {
        "suites": [
            {
                "name": "substratevm",
                "subdir": "true",
                "version": "7a35aa1db56e04bb0e5707f9f68fcbb22d28153f",
                "urls": [
                    {"url": "ssh://git@github.com:oracle/graal.git", "kind": "git"},
                ]
            },
        ]
    },

    "projects": {
        "loom.test": {
            "subDir": "src",
            "sourceDirs": ["src"],
            "dependencies": [
                "substratevm:SVM",
            ],
            "javaCompliance": "17-loom",
            "checkstyle": "com.oracle.svm.core",
            "workingSets": "SVM,Test",
        }
    }
}
