const product_channel = "767519818920230962"
const fs = require('fs'); // Import files system module
const pics = fs.readdirSync('./commands/images');
module.exports = {
	name: 'products',
	description: 'SHOP WITH US',
	execute(message, args) {

        if(message.channel.id === product_channel){
            for (const file of pics){
                message.channel.send({
                    files: [{
                        attachment: `./commands/images/${file}`,
                    }]
                })
            }


        }else{
            message.reply("THIS ISN'T THE PLACE TO ASK FOR PRODUCTS HAHAAAAHAA. TRY GOING TO THE PRODUCTS CHANNEL.")
        }

	},
};