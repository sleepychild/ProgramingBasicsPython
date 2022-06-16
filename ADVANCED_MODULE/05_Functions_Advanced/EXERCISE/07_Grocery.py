def grocery_store(**kwargs):
    return "\n".join(
        [
            f"{k}: {v}"
            for k, v in dict(
                sorted(
                    dict(
                        sorted(
                            dict(sorted(kwargs.items())).items(),
                            key=lambda x: len(x[0]),
                            reverse=True,
                        )
                    ).items(),
                    key=lambda x: x[1],
                    reverse=True,
                )
            ).items()
        ]
    )


print(
    grocery_store(
        bread=5,
        pasta=12,
        eggs=12,
    )
)

print(
    grocery_store(
        bread=2,
        pasta=2,
        eggs=20,
        carrot=1,
    )
)
