from sqlalchemy import create_engine

engine = create_engine(
    "mongobi://user?source=auth_db:12345@url:27017/cars",
    connect_args={
        "ssl": {
            "mode": "PREFERRED"
        }
    },
    pool_reset_on_return=False,
)