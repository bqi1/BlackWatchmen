const fs = require('fs'); // Import files system module

module.exports = {
	name: 'mission11',
	description: 'redacted',
	execute(message, args) {
        if (args[0] === "start"){
            fs.readFile('./commands/intros/mission11.txt','utf8',function(err,contents){
                message.channel.send(contents);
            });
        } else if ((args.join(" ").toLowerCase() === "iodine-131") || (args.join(" ").toLowerCase() === "iodine")){
            message.channel.send("That is the correct answer. Well done!")
        } else {
            message.channel.send("That answer is incorrect.")
        }

	},
};