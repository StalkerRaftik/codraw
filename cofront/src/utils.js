import $t from "@/i18n";

function isIterableObject(value) {
  return typeof value !== "string" && Symbol.iterator in Object(value);
}

export function parseResponseException(e) {
  let respContent = "";
  if (!e.response) {
    return "Соединение с сервером было прервано, попробуйте перезагрузить страницу.";
  }
  if (e.response.status >= 500) {
    return `Случилась ошибка на сервере. Сообщите об этой проблеме администратору.\nСтатус ошибки: ${e.response.status}`;
  }
  console.log(e.response.status);
  for (const errors of Object.values(e.response.data)) {
    if (!isIterableObject(errors)) {
      respContent += `- ${$t(errors)}\n`;
      continue;
    }
    errors.forEach((error) => (respContent += `- ${$t(error)}\n`));
  }
  return respContent || JSON.stringify(e.response);
}

export function showError(notification, title, exc) {
  notification.error({
    title: title,
    content: parseResponseException(exc),
    duration: 10000,
  });
}

export function changeQuerySilently(route, query) {
  let queryList = [];
  for (const entry of Object.entries(query)) {
    queryList.push(`${entry[0]}=${entry[1]}`);
  }
  history.pushState({}, "", route.path + `?${queryList.join("&")}`);
}
