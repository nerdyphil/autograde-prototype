test = {
    "name": "test1",
    "points": 0.6666666666666666,
    "hidden": True,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> import inspect
                    >>> to_base(665,8)=='1231' and 'hex(' not in inspect.getsource(to_base)
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
            ],
            "scored": False,
            "setup": "",
            "teardown": "",
            "type": "doctest"
        }
    ]
}
