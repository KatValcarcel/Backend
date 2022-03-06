import axios from "axios";

const request = axios.create({
  baseURL: `${process.env.REACT_APP_BACK_URL}`,
  headers: {
    "Content-Type": "application/json",
  },
});

export const getServerInfo = () => {
  return request.get("/api/status");
};
