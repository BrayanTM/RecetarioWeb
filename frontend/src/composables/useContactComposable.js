export function useContactComposable() {
  let sendData = async (body) => {
    try {
      let response = await fetch(`${import.meta.env.VITE_API_URL}contact/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(body),
      });

      if (!response.ok) {
        throw new Error("Network response was not ok");
      }

      window.location.reload();
    } catch (error) {
      console.error("There was a problem with the fetch operation:", error);
      throw error;
    }
  };

  return { sendData };
}
