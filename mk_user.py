from app.routes import db, User


def create_my_user(first_name, last_name, hobbies):
    db.session.add(
        User(
            first_name=first_name,
            last_name=last_name,
            hobbies=hobbies,
        )
    )
    db.session.commit()


if __name__ == "__main__":
    create_my_user("Todd", "Mickel", "Baseball")
    create_my_user("Holly", "Mickel", "Looking beautiful")
    users = User.query.all()
    print("All users:")
    print(users)
    holly = User.query.filter_by(first_name="Holly").first()
    holly.first_name = "Hunny Bunny"
    db.session.commit()
    print("Single user:")
    print(holly)
