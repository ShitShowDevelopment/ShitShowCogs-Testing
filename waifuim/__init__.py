from .waifuim import Waifu

async def setup(bot):
	await bot.add_cog(Waifu(bot))