from .discordlink import DiscordLinkCog

def setup(bot):
	await bot.add_cog(DiscordLinkCog(bot))
