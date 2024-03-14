import discord
import waifuim

from redbot.core import commands

class Waifu(commands.Cog):
        """
        Get images from Waifu.IM API
        """

        def __init__(self, bot):
                self.bot = bot
                self.session = waifuim.WaifuAioClient()
                
                async def cog_unload(self) -> None:
                        self.session.close()
                
        @commands.hybrid_command()
        @commands.bot_has_permissions(send_messages=True, embed_links=True)
        async def waifuimhelp(self, ctx):
                """
                Get the help message for the WaifuIm command
                """
                
                
                versatile_tags = '```yml{}```'.format(
                        '\n - waifu: Get a random waifu image',
                        '\n - maid: Get a random maid image',
                        '\n - marin-kitagawa: Get a random Marin Kitagawa image',
                        '\n - mori-calliope: Get a random Mori Calliope image',
                        '\n - raiden-shogun: Get a random Raiden Shogun image',
                        '\n - oppai: Get a random oppai image',
                        '\n - selfies: Get a random selfies image',
                        '\n - uniform: Get a random uniform image',
                        '\n - kamisato-ayaka: Get a random Kamisato Ayaka image'
                        )
                nsfw_tags ='```yml{}```'.format(
                        '\n - ero: Get a random ero image',
                        '\n - ass: Get a random ass image',
                        '\n - hentai: Get a random hentai image',
                        '\n - milf: Get a random milf image',
                        '\n - oral: Get a random oral image',
                        '\n - paizuri: Get a random paizuri image',
                        '\n - ecchi: Get a random ecchi image'
                        )
                command_examples = '```py{}```'.format(
                        '\n [p]tag maid',
                        '\n [p]ntag maid'
                )
                
                e = discord.Embed(
                        title='Waifu.IM',
                        description='```{}{}{}```'.format(
                                '\nBelow are the availeable tags for use with waifu.im',
                                '\nThe NSFW tags can only be used with the NSFW command(s), while the Versatile tags can be used in both SFW and NSFW command(s)',
                                '\nNSFW command(s) can only be used in NSFW channel(s)'
                                ), 
                        color=discord.Color.blue()
                        )
                e.add_field(name='Versatile Tags', value=versatile_tags, inline=True)
                e.add_field(name='NSFW Tags', value=nsfw_tags, inline=True)
                e.add_field(name='Example', value=command_examples, inline=False)
        
        
        @commands.hybrid_command()
        @commands.bot_has_permissions(send_messages=True, embed_links=True)
        async def random(self, ctx):
                """
                Get a random waifu image
                """
                
                wf = waifuim.WaifuAioClient()
                
                image = await wf.search(
                        is_nsfw='null'
                )
                
                image_url = str(image)
                image_tag = image.tags[0].name
                image_description = image.description[0]
                
                
                e = discord.Embed(description='{}'.format(image_description), color=discord.Color.blue())
                e.add_field(name='Tag', value=image_tag, inline=True)
                e.add_field(name='Direct Link', value='[Open in Browser][{}]'.format(image_url), inline=True)
                e.set_footer(text='Requested by {}'.format(ctx.author.display_name, icon_url=ctx.author.avatar_url))
                
                await wf.close()
                await ctx.send(embed=e)
                
        @commands.hybrid_command()
        @commands.bot_has_permissions(send_messages=True, embed_links=True)
        async def tag(self, *args: input, ctx):
                """
                Get a random waifu image by tag
                """
                
                wf = waifuim.WaifuAioClient()
                
                image = await wf.search(
                        tags=['{}'.format(args)],
                        is_nsfw='null'
                )
                
                image_url = str(image)
                image_tag = image.tags[0].name
                image_description = image.description[0]
                
                e = discord.Embed(description='{}'.format(image_description), color=discord.Color.blue())
                e.add_field(name='Tag', value=image_tag, inline=True)
                e.add_field(name='Direct Link', value='[Open in Browser][{}]'.format(image_url), inline=True)
                e.set_footer(text='Requested by {}'.format(ctx.author.display_name, icon_url=ctx.author.avatar_url))
                
                await wf.close()
                await ctx.send(embed=e)
                
        @commands.hybrid_command()
        @commands.bot_has_permissions(send_messages=True, embed_links=True)
        async def gif(self, ctx):
                """
                Get a random waifu gif
                """
                
                wf = waifuim.WaifuAioClient()
                
                image = await wf.search(
                        gif=True,
                        is_nsfw='null'
                )
                
                image_url = str(image)
                image_tag = image.tags[0].name
                image_description = image.description[0]
                
                e = discord.Embed(description='{}'.format(image_description), color=discord.Color.blue())
                e.add_field(name='Tag', value=image_tag, inline=True)
                e.add_field(name='Direct Link', value='[Open in Browser][{}]'.format(image_url), inline=True)
                e.set_footer(text='Requested by {}'.format(ctx.author.display_name, icon_url=ctx.author.avatar_url))
                
                await wf.close()
                await ctx.send(embed=e)
                
        @commands.hybrid_command()
        @commands.bot_has_permissions(send_messages=True, embed_links=True)
        async def dump(self, ctx):
                """
                Dump a bunch of random waifu images
                """
                
                wf = waifuim.WaifuAioClient()
                
                image = await wf.search(
                        many=True,
                        is_nsfw='null'
                )
                
                image_url = str(image)
                image_tag = image.tags[0].name
                image_description = image.description[0]
                
                e = discord.Embed(description='{}'.format(image_description), color=discord.Color.blue())
                e.add_field(name='Tag', value=image_tag, inline=True)
                e.add_field(name='Direct Link', value='[Open in Browser][{}]'.format(image_url), inline=True)
                e.set_footer(text='Requested by {}'.format(ctx.author.display_name, icon_url=ctx.author.avatar_url))
                
                await wf.close()
                await ctx.send(embed=e)
                
        @commands.hybrid_command()
        @commands.bot_has_permissions(send_messages=True, embed_links=True)
        @commands.is_nsfw()
        async def nrandom(self, ctx):
                """
                Get a random nsfw waifu image
                """
                
                wf = waifuim.WaifuAioClient()
                
                image = await wf.search(
                        is_nsfw=True
                )
                
                image_url = str(image)
                image_tag = image.tags[0].name
                image_description = image.description[0]
                
                e = discord.Embed(description='{}'.format(image_description), color=discord.Color.blue())
                e.add_field(name='Tag', value=image_tag, inline=True)
                e.add_field(name='Direct Link', value='[Open in Browser][{}]'.format(image_url), inline=True)
                e.set_footer(text='Requested by {}'.format(ctx.author.display_name, icon_url=ctx.author.avatar_url))
                
                await wf.close()
                await ctx.send(embed=e)
                                
        @commands.hybrid_command()
        @commands.bot_has_permissions(send_messages=True, embed_links=True)
        @commands.is_nsfw()
        async def ntag(self, *args: input, ctx):
                """
                Get a random nsfw waifu image by tag
                """
                
                wf = waifuim.WaifuAioClient()
                
                image = await wf.search(
                        tags=['{}'.format(args)],
                        is_nsfw=True
                )
                
                image_url = str(image)
                image_tag = image.tags[0].name
                image_description = image.description[0]
                
                e = discord.Embed(description='{}'.format(image_description), color=discord.Color.blue())
                e.add_field(name='Tag', value=image_tag, inline=True)
                e.add_field(name='Direct Link', value='[Open in Browser][{}]'.format(image_url), inline=True)
                e.set_footer(text='Requested by {}'.format(ctx.author.display_name, icon_url=ctx.author.avatar_url))
                
                await wf.close()
                await ctx.send(embed=e)
                
        @commands.hybrid_command()
        @commands.bot_has_permissions(send_messages=True, embed_links=True)
        @commands.is_nsfw()
        async def ngif(self, ctx):
                """
                Get a random nsfw waifu gif
                """
                
                wf = waifuim.WaifuAioClient()
                
                image = await wf.search(
                        gif=True,
                        is_nsfw=True
                )
                
                image_url = str(image)
                image_tag = image.tags[0].name
                image_description = image.description[0]
                
                e = discord.Embed(description='{}'.format(image_description), color=discord.Color.blue())
                e.add_field(name='Tag', value=image_tag, inline=True)
                e.add_field(name='Direct Link', value='[Open in Browser][{}]'.format(image_url), inline=True)
                e.set_footer(text='Requested by {}'.format(ctx.author.display_name, icon_url=ctx.author.avatar_url))
                
                await wf.close()
                await ctx.send(embed=e)
                
        @commands.hybrid_command()
        @commands.bot_has_permissions(send_messages=True, embed_links=True)
        @commands.is_nsfw()
        async def ndump(self, ctx):
                """
                Dump a bunch of random nsfw waifu images
                """
                
                wf = waifuim.WaifuAioClient()
                
                image = await wf.search(
                        many=True,
                        is_nsfw=True
                )
                
                image_url = str(image)
                image_tag = image.tags[0].name
                image_description = image.description[0]
                
                e = discord.Embed(description='{}'.format(image_description), color=discord.Color.blue())
                e.add_field(name='Tag', value=image_tag, inline=True)
                e.add_field(name='Direct Link', value='[Open in Browser][{}]'.format(image_url), inline=True)
                e.set_footer(text='Requested by {}'.format(ctx.author.display_name, icon_url=ctx.author.avatar_url))
                
                await wf.close()
                await ctx.send(embed=e)