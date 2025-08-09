import axios from 'axios';

const API = axios.create({
  baseURL: '/api', // This gets proxied to localhost:8080
});

export default API;
