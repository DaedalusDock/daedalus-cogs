from .deebee import DeeBee

def setup(bot):
	await bot.add_cog(DeeBee(bot))
