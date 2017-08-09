# -*- coding: utf-8 -*-

"""
The MIT License (MIT)

Copyright (c) 2017-2017 Mgardne8

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from .object import Object

class Webhook(Object):
    """Represents a webhook.

    Depending on the way this object was created, some of the attributes can
    have a value of ``None``.


    Attributes
    -----------
    name: str
        The name of the webhook.
    id: int
        The webhooks's ID.
    avatar:
        The webhook's Avatar
    owner_id:
        the id of the user that that webhook belongs too
    channel_id:
        the id of the channel that the webhook belongs too
    guild_id:
        The id of the guild that the webhook belongs too
    token:
        The secure token of the webhook (if given)
    """
    __slots__ = ('name', 'id', 'avatar', 'owner_id', 'channel_id', 'guild_id', 'token')

    def __init__(self, data):
        self._update(data)

    def _update(self,data):
        self.id = data['id']
        self.name = data['name'],
        self.token = data['token'],
        self.avatar = data['avatar'],
        self.guild_id = data['guild_id'],
        self.owner_id = data['user']['id'],
        self.channel_id = data['channel_id'],

    def _delete(self):
        raise NotImplementedError('Todo')

    @asyncio.coroutine
    def edit(self, name, *, avatar=None):
        """|coro|
        edits the webhook

        Raises
        ------
        Forbidden
            You do not have proper permissions to edit this webhook.
        HTTPException
            An error occurred while editing the webhook, or this webhook does not exist.

        Returns
        -------
        :class:'Webhook' or `None`

        Returns
        --------
        :class:'Webhook'
            self
        """

        data = yield from self._state.http.edit_webhook(webhook_id=webhook_id, name=name, avatar=avatar)
        self._update(data)
        return self

    @asyncio.coroutine
    def delete(self):
        """|coro|
        deletes the webhook

        Raises
        -------
        Forbidden
            You do not have proper permissions to delete this webhook.
        HTTPException
            An error occurred while deleting the webhook, or this webhook does not exist.

        Returns
        --------
        `None`
        """

        data = yield from self._state.http.delete_webhook(webhook_id=webhook_id)
        self._delete
        return None