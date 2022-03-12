const RU = {
  // Global
  true: "Да",
  false: "Нет",

  // Profile
  id: "Идентификатор",
  username: "Имя пользователя",
  password: "Пароль",
  email: "Почта",
  is_staff: "Администратор",
  last_login: "В последний раз заходил",

  // Registration TODO: Translate such errors on server
  "A user with that username already exists.":
    "Пользователь с таким именем уже существует.",
  "This password is too short. It must contain at least 8 characters.":
    "Пароль слишком короткий. Он должен состоять из 8 символов или более.",
  "This password is too common.": "Ваш пароль слишком уязвим для взлома.",
  "This password is entirely numeric.":
    "Пароль не должен состоять из одних цифр",
  'Incorrect login or password!': 'Неправильный логин или пароль!',
};

const BASE_LANG = RU;

export default function $t(text) {
  if (typeof text !== "string") {
    text = text?.toString().trim().toLowerCase();
  }
  return BASE_LANG[text] || text;
}
