class BaseRepository {
    constructor(model) {
        this.model = model;
    }

    async getAll(options = {}) {
        return this.model.findAll(options);
    }

    async getById(id, options = {}) {
        return this.model.findByPk(id, options);
    }

    async create(data, options = {}) {
        return this.model.create(data, options);
    }

    async update(id, data, options = {}) {
        const record = await this.getById(id, options);
        if (record) {
            return record.update(data, options);
        }
        return null;
    }

    async delete(id, options = {}) {
        const record = await this.getById(id, options);
        if (record) {
            await record.destroy(options);
            return true;
        }
        return false;
    }
}

module.exports = BaseRepository;
