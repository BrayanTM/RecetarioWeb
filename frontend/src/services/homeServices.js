export async function getDataHome() {
  let response = await fetch(`${import.meta.env.VITE_API_URL}recipes/home/`, {headers: {
    'Content-Type': 'application/json',
  }});
  let data = await response.json();
  return data;
}
