import axios from "axios";

const API_URL = "http://localhost:5050/api/auth/";

class AuthService {
  login(user) {

    const fd = new FormData();

    fd.append("username", user.username);
    fd.append("password", user.password);


    return axios
      .post(API_URL + "login", fd)
      .then(response => {
        if (response.data.token) {
          localStorage.setItem("user", JSON.stringify(response.data));
        }

        return response.data;
      });
  }

  logout() {
    localStorage.removeItem("user");
  }

  register(user) {
    const fd = new FormData();

    fd.append("username", user.username);
    fd.append("email", user.email);
    fd.append("first_name", user.fName);
    fd.append("last_name", user.lName);
    fd.append("password", user.password);
    fd.append("biography", user.biography);
    fd.append("location", user.location);
    fd.append("photo", user.photo);


    return axios.post("http://localhost:5050/api/" + "register", fd);
  }
}

export default new AuthService();
