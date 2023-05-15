from .deebee import DeeBee

async def setup(bot):
	await bot.add_cog(DeeBee(bot))
