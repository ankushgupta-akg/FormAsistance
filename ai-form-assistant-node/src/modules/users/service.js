const userRepository = require("./repository");
const sequelize = require("../../database/sequelize");

class UserService {

    async getUsers() {
        return userRepository.getAll();
    }

    async getUser(id) {
        return userRepository.getById(id);
    }

    async createUser(data) {
        const t = await sequelize.transaction();
        try {
            const user = await userRepository.create(data, { transaction: t });
            await t.commit();
            return user;
        } catch (error) {
            await t.rollback();
            throw error;
        }
    }

    async deleteUser(id) {
        const t = await sequelize.transaction();
        try {
            const result = await userRepository.delete(id, { transaction: t });
            await t.commit();
            return result;
        } catch (error) {
            await t.rollback();
            throw error;
        }
    }

}

module.exports = new UserService();