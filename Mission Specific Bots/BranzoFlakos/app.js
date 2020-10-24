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
    console.log("Branzo online.");
});


client.on('message',message =>{

    if (message.author.bot) return;

    if (message.channel.type === "dm"){
        if (message.content.toLowerCase().includes("joe") && message.content.toLowerCase().includes("brain branzo flaks") && message.content.toLowerCase().includes("vancouver") && message.content.toLowerCase().includes("canucks") && message.content.toLowerCase().includes("bicycling") && message.content.toLowerCase().includes("pretzels") && message.content.toLowerCase().includes("mountain dew") ){
            // The right asking
            setTimeout(function(){ message.author.send("Hey there "+message.author.username+"!\nThat's no problem, we have so many interns, one is bound to lose their code.\nSorry for not recognizing your username, since everyone is applying via their Discord username, there's too many to keep track of. I'll look for yours as soon as I'm done with some files.\nIn the meantime, here is the access code: 29583\nGoing bicycling sounds fun! I'll see you soon!"); }, 30000);
        } else{
            // A dm, but not the right asking
            setTimeout(function(){
                message.author.send("Hi there! Directly messaging this bot alerts our one person staff. Unfortunately, he has deemed your message as more suited for customer inquiries, resulting in this automated message. Kindly go to that channel! HAPPY CEREAL HUNTING");
        }, 10000);

        }

    }

    if (!message.content.startsWith(prefix))return;


    const args = message.content.slice(prefix.length).trim().split(/ +/);
    const command = args.shift().toLowerCase();
    try {
        client.commands.get(command).execute(message,args);
    } catch (error) {
        console.log(error);
        message.reply("Sorry, that's not a valid command! WE LOVE YOU THOuGH.");
    }
    
});

client.login(token)