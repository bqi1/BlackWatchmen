const {token,prefix} = require("./configuration.json");
const fs = require('fs'); // Import files system module
const Discord = require("discord.js");
const client = new Discord.Client();
client.commands = new Discord.Collection(); 
const commandFiles = fs.readdirSync('./commands').filter(file => file.endsWith('.js')); // Retrieve all command files
for (const file of commandFiles) {
    const command = require(`./commands/${file}`);
    client.commands.set(command.name,command);
}

client.once('ready',() =>{
    console.log("Missions online.");
});


client.on('guildMemberAdd', member => {
    fs.readFile('./Intro.txt','utf8',function(err,contents){
        member.send(contents);
    });
});

client.on('message',message =>{
    if (!message.content.startsWith(prefix) || message.author.bot || !(message.channel.type === "dm")) return;
    const args = message.content.slice(prefix.length).trim().split(/ +/);
    const command = args.shift().toLowerCase();
    try {
        client.commands.get(command).execute(message,args);
        console.log(message.author.username+command);
    } catch (error) {
        message.reply("Invalid command.")
    }
});

client.login(token)