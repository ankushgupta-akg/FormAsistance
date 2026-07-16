const userService = require("./service");

class UserController {

    async getUsers(req, res) {
        const users = await userService.getUsers();
        res.json(users);
    }

    async getUser(req, res) {
        const user = await userService.getUser(req.params.id);
        if (!user) {
            return res.status(404).json({ error: "User not found" });
        }
        res.json(user);
    }

}

module.exports = new UserController();