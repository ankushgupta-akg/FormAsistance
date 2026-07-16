const { DataTypes } = require("sequelize");
const sequelize = require("../../database/sequelize");

const User = sequelize.define(
    "User",
    {
        id: {
            type: DataTypes.UUID,
            autoIncrement: true,
            primaryKey: true,
        },

        username: {
            type: DataTypes.STRING(100),
            allowNull: false,
            unique: true,
        },

        password: {
            type: DataTypes.STRING(255),
            allowNull: false,
        },

        full_name: {
            type: DataTypes.STRING(255),
            allowNull: false,
        },
    },
    {
        tableName: "users",
        underscored: true,
        timestamps: true,
    }
);

module.exports = User;