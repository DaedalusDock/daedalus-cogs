from .discordlink import DiscordLinkCog

async def setup(bot):
	await bot.add_cog(DiscordLinkCog(bot))
